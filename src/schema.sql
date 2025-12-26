-- 1. Vytvoření databáze
CREATE DATABASE IF NOT EXISTS online_learning_platform;
USE online_learning_platform;

-- 2. Tabulka: INSTRUCTORS
CREATE TABLE instructors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    bio TEXT,
    rating FLOAT DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    CONSTRAINT chk_rating CHECK (rating >= 0 AND rating <= 5)
);

-- 3. Tabulka: COURSES
CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    instructor_id INT NOT NULL,
    price FLOAT NOT NULL DEFAULT 0,
    duration_hours FLOAT NOT NULL,
    level ENUM('Beginner', 'Intermediate', 'Advanced', 'Expert', 'Master') NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES instructors(id) ON DELETE CASCADE
);

-- 4. Tabulka: STUDENTS
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    registration_date DATE NOT NULL
);

-- 5. Tabulka: ENROLLMENTS (Vazební tabulka M:N)
CREATE TABLE enrollments (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    progress_percentage FLOAT DEFAULT 0,
    final_score FLOAT DEFAULT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    CONSTRAINT chk_progress CHECK (progress_percentage >= 0 AND progress_percentage <= 100)
);

-- 6. Tabulka: CERTIFICATES
CREATE TABLE certificates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    issue_date DATE NOT NULL,
    certificate_number VARCHAR(50) NOT NULL UNIQUE,
    is_verified BOOLEAN DEFAULT TRUE,
    -- Vazba na enrollment přes složený klíč
    FOREIGN KEY (student_id, course_id) REFERENCES enrollments(student_id, course_id) ON DELETE CASCADE
);

-- ---------------------------------------------------------
-- POHLEDY (VIEWS)
-- ---------------------------------------------------------

-- Pohled 1: Pokrok studentů
CREATE OR REPLACE VIEW student_progress AS
SELECT 
    s.name AS student_name,
    c.title AS course_title,
    i.name AS instructor_name,
    e.progress_percentage,
    e.is_completed,
    e.enrollment_datetime
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
JOIN instructors i ON c.instructor_id = i.id;

-- Pohled 2: Nejlépe hodnocené kurzy (top_rated_courses)
CREATE OR REPLACE VIEW top_rated_courses AS
SELECT 
    c.title AS course_title,
    i.name AS instructor_name,
    i.rating AS instructor_rating,
    c.level,
    c.price,
    COUNT(e.student_id) AS total_students
FROM courses c
JOIN instructors i ON c.instructor_id = i.id
LEFT JOIN enrollments e ON c.id = e.course_id
WHERE c.is_published = TRUE
GROUP BY c.id
ORDER BY i.rating DESC, total_students DESC;

-- ---------------------------------------------------------
-- TESTOVACÍ DATA (VOLITELNÉ)
-- ---------------------------------------------------------

INSERT INTO instructors (name, email, bio, rating, is_verified) VALUES
('Jan Novák', 'jan.novak@email.cz', 'Expert na Python a Data Science', 4.8, TRUE),
('Petr Svoboda', 'petr.svoboda@email.cz', 'Webový vývojář s 10 lety praxe', 4.5, FALSE);

INSERT INTO courses (title, instructor_id, price, duration_hours, level, is_published) VALUES
('Python pro začátečníky', 1, 499.0, 20.5, 'Beginner', TRUE),
('Moderní JavaScript', 2, 0, 15.0, 'Intermediate', TRUE);

INSERT INTO students (name, email, registration_date, is_premium) VALUES
('Martin Dvořák', 'martin@email.cz', CURDATE(), FALSE),
('Lucie Černá', 'lucie@email.cz', CURDATE(), TRUE);

INSERT INTO enrollments (student_id, course_id, progress_percentage, is_completed) VALUES
(1, 1, 50.0, FALSE),
(2, 1, 100.0, TRUE);

INSERT INTO certificates (student_id, course_id, issue_date, certificate_number) VALUES
(2, 1, CURDATE(), 'CERT-PY-2025-001');
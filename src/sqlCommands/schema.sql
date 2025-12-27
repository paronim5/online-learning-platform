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

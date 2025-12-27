INSERT INTO instructors (name, email, bio, rating, is_verified) VALUES
('Jan Novák', 'jan.novak@email.cz', 'Expert na Python a Data Science', 4.8, TRUE),
('Petr Svoboda', 'petr.svoboda@email.cz', 'Webový vývojář s 10 lety praxe', 4.5, FALSE);

INSERT INTO courses (title, instructor_id, price, duration_hours, level) VALUES
('Python pro začátečníky', 1, 499.0, 20.5, 'Beginner'),
('Moderní JavaScript', 2, 0, 15.0, 'Intermediate');

INSERT INTO students (name, email, registration_date) VALUES
('Martin Dvořák', 'martin@email.cz', CURDATE()),
('Lucie Černá', 'lucie@email.cz', CURDATE());

INSERT INTO enrollments (student_id, course_id, progress_percentage, is_completed) VALUES
(1, 1, 50.0, FALSE),
(2, 1, 100.0, TRUE);

INSERT INTO certificates (student_id, course_id, issue_date, certificate_number) VALUES
(2, 1, CURDATE(), 'CERT-PY-2025-001');
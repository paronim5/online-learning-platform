
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
GROUP BY c.id
ORDER BY i.rating DESC, total_students DESC;

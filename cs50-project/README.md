# Campus Hub

#### Video Demo: https://youtu.be/AFjBLHJnfxk?si=dIUzv_UYXAEADD5D

#### Description:
Campus Hub is a web-based student management application developed as my CS50x Final Project. The goal of this project is to provide university students with a single platform where they can organize their academic activities efficiently. Instead of managing subjects, notes, assignments, attendance, and timetables across different applications, Campus Hub combines all of these essential features into one simple and user-friendly interface.

The application focuses on improving organization and productivity by allowing students to keep track of their daily academic tasks. It was designed with simplicity, usability, and clean visual aesthetics in mind so that users can easily navigate through the system without unnecessary complexity.

## Why I Chose This Project

I chose to build Campus Hub because I wanted to create a project that solves a real problem faced by many university students. During my studies, I noticed that students often use different applications to manage their notes, assignments, attendance records, and study schedules. Switching between multiple platforms can be inconvenient and makes it difficult to stay organized.

My goal was to design a single application where all essential academic tools are available in one place. Rather than creating a project with only one primary function, I wanted to develop a complete student portal that demonstrates the practical concepts I learned throughout CS50x, including databases, authentication, CRUD operations, templates, routing, and responsive web design.

This project also gave me the opportunity to strengthen my understanding of Flask, SQL, HTML, CSS, Bootstrap, and JavaScript while building something that could be useful beyond the scope of the course.

## Features

### User Authentication

Campus Hub provides a secure user authentication system that allows users to register for a new account, log in using their credentials, and log out safely. User sessions are managed using Flask sessions, ensuring that each user can only access their own data.

### Dashboard

The dashboard serves as the central page of the application. It provides a quick overview of the user's academic information by displaying the total number of subjects, notes, assignments, and pending assignments. This gives users an instant summary of their academic progress.

### Subject Management

Users can create, edit, delete, and search subjects. Each subject acts as a category that organizes notes, assignments, attendance records, and timetable entries. This structure keeps all academic information well organized.

### Notes Management

The notes module allows users to save study notes for each subject. Notes can be edited, deleted, and searched whenever required, making it easier to organize study material throughout the semester.

### Assignment Tracker

Users can add assignments with their respective subjects and due dates. Assignments can be edited, deleted, marked as completed, and searched. This feature helps students keep track of deadlines and unfinished work.

### Attendance Management

The attendance module allows students to record attendance for each subject. Existing records can be updated or removed whenever necessary, providing a simple way to maintain attendance information.

### Timetable Management

The timetable feature enables users to manage their weekly class schedule by storing the subject name, day, and class timing. Users can add, edit, delete, and search timetable entries whenever needed.

### Search Functionality

Campus Hub includes search functionality across different modules, allowing users to quickly find subjects, notes, assignments, attendance records, and timetable entries without manually browsing through large amounts of data.

### Responsive User Interface

The application is designed using Bootstrap 5 together with custom CSS to provide a clean, responsive, and user-friendly interface. The soft pink theme and consistent layout create a modern appearance while maintaining simplicity and ease of use.

## Database Design

Campus Hub uses SQLite as its database management system. The database is designed to keep each user's academic information separate and organized. Every major feature of the application stores its data in a dedicated table, while relationships between tables ensure data consistency.

### Users Table

The `users` table stores account information for registered users. Each user has a unique ID, username, and a securely hashed password. Passwords are never stored in plain text, improving the security of the application.

### Subjects Table

The `subjects` table stores all subjects created by a user. Each subject is linked to its owner using the `user_id` field. This ensures that users can only access and manage their own subjects.

### Notes Table

The `notes` table stores study notes associated with individual subjects. Every note references a subject through `subject_id`, creating a one-to-many relationship between subjects and notes.

### Assignments Table

The `assignments` table stores assignment information, including the assignment title, due date, completion status, and associated subject. This allows users to organize assignments according to their subjects and monitor pending work.

### Attendance Table

The `attendance` table stores attendance records for each subject. Users can record attendance percentages or related information while keeping it linked to the correct subject.

### Timetable Table

The `timetable` table stores weekly class schedules. Each timetable entry contains the subject, day, and class timing, allowing users to manage their study schedule efficiently.

The relationships between these tables make the application modular, organized, and easy to maintain while preventing unnecessary duplication of data.

## Design Decisions

While developing Campus Hub, I made several design decisions to ensure that the application remained simple, organized, and easy to use.

### Flask

I chose Flask as the backend framework because it is lightweight, flexible, and integrates well with SQLite databases. Flask also provides a clear routing system and template engine, making it suitable for building a structured web application.

### SQLite

SQLite was selected because it is simple to set up, requires no separate database server, and is fully sufficient for a student management application. Since the application is intended for individual users, SQLite provides an efficient and reliable solution.

### Bootstrap

Bootstrap 5 was used to create a responsive layout without writing excessive CSS. It allowed me to design forms, tables, navigation bars, buttons, and alerts with a consistent appearance across different screen sizes.

### User Authentication

A login and registration system was implemented so that each user's data remains private. Passwords are stored as hashed values instead of plain text, improving the security of the application.

### Dashboard

Instead of displaying raw database records immediately after login, I designed a dashboard that summarizes important academic information. Displaying the total number of subjects, notes, assignments, and pending assignments provides users with a quick overview of their academic progress.

### User Interface

I selected a soft pink color palette to give the application a clean, modern, and welcoming appearance. The interface was intentionally kept simple so that students can focus on managing their academic information without unnecessary distractions.

### Search Functionality

Search features were added to improve usability by allowing users to quickly locate specific records instead of manually browsing through long tables. This makes the application more practical as the amount of stored data grows.

Throughout the development process, I prioritized readability, simplicity, and ease of navigation. Every feature was designed to minimize user effort while maintaining a consistent interface across the application.

## Challenges Faced During Development

Developing Campus Hub was both challenging and rewarding. Since this was my first complete web application built with Flask, I encountered several problems throughout the development process.

One of the biggest challenges was designing the database relationships correctly. I needed to ensure that every subject, note, assignment, attendance record, and timetable entry belonged to the correct user while maintaining proper relationships between tables. Understanding foreign keys and writing SQL queries to retrieve related data required careful planning.

Another challenge was implementing CRUD (Create, Read, Update, Delete) functionality for every module. Although the overall structure was similar across different sections, each feature required its own routes, SQL queries, HTML templates, and validation logic. Debugging routing errors, template issues, and database queries helped me better understand how Flask applications are structured.

Creating a clean and consistent user interface was also an important part of the project. I experimented with different layouts, button styles, colors, and navigation designs before choosing a soft pink theme that provides a modern and user-friendly experience while maintaining readability.

Throughout development, debugging became an essential learning experience. I encountered issues related to routing, template rendering, endpoint naming, URL generation, and HTML structure. Solving these problems improved my problem-solving skills and strengthened my understanding of how different parts of a web application work together.

Overall, this project allowed me to combine everything I learned throughout CS50x, including Python, SQL, HTML, CSS, JavaScript, Flask, and database management, into one complete application. It also gave me valuable experience in organizing a larger codebase and building a project from the initial idea to the final implementation.


## Future Improvements

Although Campus Hub currently provides the core features required for managing academic activities, there are several improvements that could be added in future versions.

One possible enhancement is implementing deadline reminders and notifications for upcoming assignments and important events. This would help students stay informed without manually checking the application.

Another improvement would be allowing users to upload files or images with their notes, making the application more useful for storing lecture slides, PDFs, and other study materials.

A calendar view could also be integrated to display assignments, classes, and important dates in a more visual and interactive way.

Future versions could include attendance percentage calculations, GPA tracking, exam scheduling, and progress analytics to provide students with a more comprehensive academic management system.

Additional improvements such as dark mode, profile customization, mobile optimization, email verification, password reset functionality, and cloud database support would further enhance both the user experience and the scalability of the application.

Overall, Campus Hub has been designed with future expansion in mind, making it possible to introduce new features while maintaining a clean and organized project structure.

## Conclusion

Campus Hub represents the successful integration of the concepts learned throughout CS50x into a practical, real-world application. Building this project allowed me to strengthen my understanding of web development, database management, user authentication, and responsive interface design.

Beyond improving my technical skills, this project taught me how to approach larger software projects by breaking them into smaller, manageable components. It also reinforced the importance of debugging, planning, and writing clean, maintainable code.

Developing Campus Hub has been a rewarding learning experience, and I look forward to continuing to improve the application by adding new features and refining the overall user experience in future versions.

## Acknowledgements

This project was developed as the final project for Harvard University's CS50x: Introduction to Computer Science. I would like to thank Professor David J. Malan and the entire CS50 team for creating an engaging and inspiring learning experience that helped me build this application.

# 24AMPT401 – Web Development Framework Laboratory

**Institution:** Sri Sai Ram Engineering College, Chennai  
**Department:** CSE (Artificial Intelligence & Machine Learning)  
**Semester:** IV Semester | Academic Year: 2025–2026

---

## Course Outcomes

| CO | Description |
|----|-------------|
| CO1 | Apply HTML and CSS to create interactive and dynamic websites |
| CO2 | Use JavaScript to develop interactive and dynamic website features |
| CO3 | Design and implement dynamic server-side applications using PHP |
| CO4 | Analyze Node.js and its features for efficient application development |
| CO5 | Develop applications using MongoDB for database management and storage |
| CO6 | Analyze and evaluate the features of Express and React for building web applications |

---

## List of Experiments

| Ex No | Title | Tech | File(s) |
|-------|-------|------|---------|
| 01 | User Registration Form | HTML | `ex01_html_registration/registration.html` |
| 02 | CSS Box Model and Background Properties | HTML, CSS | `ex02_css_boxmodel/` |
| 03 | CSS Animations and Multi-Column Layout | HTML, CSS | `ex03_css_animations/` |
| 04 | JavaScript Data Types | HTML, JS | `ex04_js_datatypes/datatypes.html` |
| 05 | Sum of Even Numbers in Array | HTML, JS | `ex05_js_even_sum/evenSum.html` |
| 06 | HTML Form with Validation | HTML | `ex06_html_form_validation/form_validation.html` |
| 07 | PHP Variables, Data Types, Constants | PHP | `ex07_php_datatypes/datatypes.php` |
| 08 | PHP Max Value in Array | PHP | `ex08_php_max_array/maxValue.php` |
| 09 | PHP Image File Upload Handling | HTML, PHP | `ex09_php_file_upload/` |
| 10 | Node.js Hello World | Node.js | `ex10_nodejs_hello/hello.js` |
| 11 | Node.js EventEmitter and setTimeout | Node.js | `ex11_nodejs_eventemitter/eventEmitter.js` |
| 12 | Node.js Callback Function | Node.js | `ex12_nodejs_callback/callbackSum.js` |
| 13 | Node.js File Reading using fs Module | Node.js | `ex13_nodejs_fs/` |
| 14 | MongoDB Installation and Database Creation | MongoDB | `ex14_mongodb_setup/` |
| 15 | MongoDB Collection Creation and Document Insertion | MongoDB | `ex15_mongodb_collection/` |
| 16 | Node.js Connect MongoDB and Retrieve Data | Node.js, MongoDB | `ex16_nodejs_mongodb/` |
| 17 | Express.js Server Creation and Routing | Node.js, Express | `ex17_expressjs_server/` |
| 18 | React Counter Component | React | `ex18_react_counter/` |
| 19 | React Router – Home and About Pages | React | `ex19_react_router/` |
| 20 | React ToggleText Component | React | `ex20_react_toggle/` |

---

## How to Run

### HTML / CSS (Ex 01–06)
Open the `.html` file directly in any web browser.

### PHP (Ex 07–09)
Requires a PHP server (XAMPP / WAMP / Laravel Herd).
```bash
# Place files in htdocs (XAMPP) and access via:
http://localhost/ex07_php_datatypes/datatypes.php
```

### Node.js (Ex 10–13, 16–17)
Requires [Node.js](https://nodejs.org/) installed.
```bash
node hello.js          # Ex 10
node eventEmitter.js   # Ex 11
node callbackSum.js    # Ex 12
node readFile.js       # Ex 13
```

For Ex 16 (MongoDB driver) and Ex 17 (Express):
```bash
npm install    # Install dependencies
npm start      # Run the program
```

### MongoDB (Ex 14–15)
Requires [MongoDB Community Server](https://www.mongodb.com/try/download/community).
```bash
mongod         # Start server
mongosh        # Open shell, then paste commands from the .js files
```

### React (Ex 18–20)
Requires Node.js installed.
```bash
npx create-react-app my-app
cd my-app
# Copy the provided App.js (and other .js files) into src/
npm start
```

---

## Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Backend:** PHP, Node.js, Express.js
- **Database:** MongoDB
- **UI Library:** React.js

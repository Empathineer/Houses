# Houses
Program that parses and transfer student data from a csv into an sql database and then produce class rosters.

<h2><a data-id="" href="#background">Background</a></h2>

<p>Hogwarts is in need of a student database. For years, the professors have been maintaing a CSV file containing all of the students’ names and houses and years. But that file didn’t make it particularly easy to get access to certain data, such as a roster of all the Ravenclaw students, or an alphabetical listing of the students enrolled at the school.</p>

<p>The challenge ahead of you is to import all of the school’s data into a SQLite database, and write a Python program to query that database to get house rosters for each of the houses of Hogwarts.</p>

<h2><a data-id="" href="#specification">Specification</a></h2>

<li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Your program should accept the name of a CSV file as a command-line argument.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>If the incorrect number of command-line arguments are provided, your program should print an error and exit.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>You may assume that the CSV file will exist, and will have columns <code class="highlighter-rouge">name</code>, <code class="highlighter-rouge">house</code>, and <code class="highlighter-rouge">birth</code>.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>For each student in the CSV file, insert the student into the <code class="highlighter-rouge">students</code> table in the <code class="highlighter-rouge">students.db</code> database.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>While the CSV file provided to you has just a <code class="highlighter-rouge">name</code> column, the database has separate columns for <code class="highlighter-rouge">first</code>, <code class="highlighter-rouge">middle</code>, and <code class="highlighter-rouge">last</code> names. You’ll thus want to first parse each name and separate it into first, middle, and last names. You may assume that each person’s name field will contain either two space-separated names (a first and last name) or three space-separated names (a first, middle, and last name). For students without a middle name, you should leave their <code class="highlighter-rouge">middle</code> name field as <code class="highlighter-rouge">NULL</code> in the table.</li>
    </ul>
  </li>
  
 <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>For each student in the CSV file, insert the student into the <code class="highlighter-rouge">students</code> table in the <code class="highlighter-rouge">students.db</code> database.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>While the CSV file provided to you has just a <code class="highlighter-rouge">name</code> column, the database has separate columns for <code class="highlighter-rouge">first</code>, <code class="highlighter-rouge">middle</code>, and <code class="highlighter-rouge">last</code> names. You’ll thus want to first parse each name and separate it into first, middle, and last names. You may assume that each person’s name field will contain either two space-separated names (a first and last name) or three space-separated names (a first, middle, and last name). For students without a middle name, you should leave their <code class="highlighter-rouge">middle</code> name field as <code class="highlighter-rouge">NULL</code> in the table.</li>
    </ul>
  </li>
  
  <p>In <code class="highlighter-rouge">roster.py</code>, write a program that prints a list of students for a given house in alphabetical order.</p>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Your program should accept the name of a house as a command-line argument.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>If the incorrect number of command-line arguments are provided, your program should print an error and exit.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Your program should then print out each student’s full name and birth year (formatted as, e.g., <code class="highlighter-rouge">Harry James Potter, born 1980</code> or <code class="highlighter-rouge">Luna Lovegood, born 1981</code>).
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Each student should be printed on their own line.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Students should be ordered by last name. For students with the same last name, they should be ordered by first name.</li>
    </ul>
  </li>

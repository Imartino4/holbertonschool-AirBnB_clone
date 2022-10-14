<h1> HBnB - AirBnB clone </h1>

<h2> Description of the project </h2>
<p>The aim of this project is to replicate the Airbnb's web application</p>
<p>During this first step we write the BaseModel class which takes care of the initialization and the update of
the instances. This class is also the parent class of other classes needed to the web funcionality, which are: User, State, City, Place, Amenity and Review.</p>
<p>We also make command interpreter to manage all the neccesary objects. </p>

<h2> Command interpreter </h2>
<p> Besides the typical commands like quit, help and EOF, this console was customized to works with different commands to create and modifify 
objects of the different classes.</p>
<p>creates - initialize a new class and print the corresponding id.<pre><code>create 'classname'</code></pre> </p>
<p>show - prints the string representation of the instance. <pre><code>show 'classname' 'id'</code></pre></p>
<p>destroy - deletes an instance. <pre><code>destroy 'classname'  'id'</code></pre> </p>
<p>all - print the string representation of all instances or a specific class instance. <pre><code>all 'classname'  ||  all</pre></code></p>
<p>update - update an instance, adding or updating a specific attribute<pre><code> update 'classname'  'id'  'attribute_name'  'attribute_value'</code></pre></p>

<h2>Example</h2>
<pre><code>
root@aba1ef7f7e57:~/holbertonschool-AirBnB_clone# ./console.py
(hbnb)create City
bdd5d584-f64f-459a-a426-b47ff0156758

(hbnb)show City bdd5d584-f64f-459a-a426-b47ff0156758
[City] (bdd5d584-f64f-459a-a426-b47ff0156758) {'id': 'bdd5d584-f64f-459a-a426-b47ff0156758', 'created_at': datetime.datetime(2022, 10, 14, 9, 20, 51, 172752), 'updated_at': datetime.datetime(2022, 10, 14, 9, 20, 51, 172764)}

(hbnb)create Place
3ab99f82-31db-4725-8501-4cc6723d46d4

(hbnb)update City bdd5d584-f64f-459a-a426-b47ff0156758 name Montevideo

(hbnb)show City bdd5d584-f64f-459a-a426-b47ff0156758
[City] (bdd5d584-f64f-459a-a426-b47ff0156758) {'id': 'bdd5d584-f64f-459a-a426-b47ff0156758', 'created_at': datetime.datetime(2022, 10, 14, 9, 20, 51, 172752), 'updated_at': datetime.datetime(2022, 10, 14, 9, 20, 51, 172764), 'name': 'Montevideo'}

(hbnb)all
["[City] (bdd5d584-f64f-459a-a426-b47ff0156758) {'id': 'bdd5d584-f64f-459a-a426-b47ff0156758', 'created_at': datetime.datetime(2022, 10, 14, 9, 20, 51, 172752), 'updated_at': datetime.datetime(2022, 10, 14, 9, 20, 51, 172764), 'name': 'Montevideo'}",
"[Place] (3ab99f82-31db-4725-8501-4cc6723d46d4) {'id': '3ab99f82-31db-4725-8501-4cc6723d46d4', 'created_at': datetime.datetime(2022, 10, 14, 9, 21, 22, 4262), 'updated_at': datetime.datetime(2022, 10, 14, 9, 21, 22, 4280)}"]

(hbnb)destroy City bdd5d584-f64f-459a-a426-b47ff0156758

(hbnb)all
["[Place] (3ab99f82-31db-4725-8501-4cc6723d46d4) {'id': '3ab99f82-31db-4725-8501-4cc6723d46d4', 'created_at': datetime.datetime(2022, 10, 14, 9, 21, 22, 4262), 'updated_at': datetime.datetime(2022, 10, 14, 9, 21, 22, 4280)}"]

(hbnb)quit
root@aba1ef7f7e57:~/holbertonschool-AirBnB_clone#
</code></pre>

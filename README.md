<h1 align = "center"> HBnB - AirBnB clone </h1>


<p align = "center"> <img src="https://user-images.githubusercontent.com/102921918/195964129-5ceba7c0-69be-498a-ac89-41b4cd5cc210.png" /></p>

<h2> Description of the project </h2>
<p>The aim of this project is to replicate the Airbnb's web application, it will be implemented in Python.</p>
<p>During this first step the BaseModel class was created which takes care of the initialization and the update of
the instances. This class is also the parent class of other classes needed to the web funcionality, which are: User, State, City, Place, Amenity and Review.</p>
<p> The FileStorage class has the methods to save the created objects in a JSON file to keep them once the program ends which could be reloaded when the program restarts.
<br>

<h2> Command interpreter </h2>
<p>A command interpreter was made to manage all the neccesary objects. This console was created using the cmd class provided by python. </p>
<p>Besides the typical commands like quit, help and EOF, this console was customized to works with different commands to create and modifify 
objects of the different classes.</p>
<p> To run the console is needed to execute the console.py file.</p><br>
Commands:
<ul>
<p><li>creates - initialize a new class and print the corresponding id.</li><br><pre><code >create 'classname'</code></pre> </p>
<p><li>show - prints the string representation of the instance.</li><br> <pre><code>show 'classname' 'id'</code></pre></p>
<p><li>destroy - deletes an instance.</li> <br><pre><code>destroy 'classname'  'id'</code></pre> </p>
<p><li>all - print the string representation of all instances or a specific class instance.</li><br> <pre><code>all 'classname'  ||  all</pre></code></p>
<p><li>update - update an instance, adding or updating a specific attribute</li><br><pre><code> update 'classname'  'id'  'attribute_name'  'attribute_value'</code></pre></p></ul>
<br>

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
<br>

<h2> Improving the console funcionality</h2>
<p> To improve the usability of the console, differents commands were added to list, count, show, destroy and update different instances, 
 using the method call syntax of classes:</p>
 <p>Examples</p>
 <pre><code>
 root@aba1ef7f7e57:~/holbertonschool-AirBnB_clone# ./console.py
 
 
(hbnb)create BaseModel
2d176077-19c4-4d8e-b781-0b23af66b1ad

(hbnb)create User
a98d1ce8-3f9c-400e-9027-97bbfd7b41e5

(hbnb)all
["[BaseModel] (2d176077-19c4-4d8e-b781-0b23af66b1ad) {'id': '2d176077-19c4-4d8e-b781-0b23af66b1ad', 'created_at': datetime.datetime(2022, 10, 17, 5, 54, 2, 185981), 'updated_at': datetime.datetime(2022, 10, 17, 5, 54, 2, 186010)}",
"[User] (a98d1ce8-3f9c-400e-9027-97bbfd7b41e5) {'id': 'a98d1ce8-3f9c-400e-9027-97bbfd7b41e5', 'created_at': datetime.datetime(2022, 10, 17, 5, 54, 59, 745061), 'updated_at': datetime.datetime(2022, 10, 17, 5, 54, 59, 745076)}"]

(hbnb)User.all()
["[User] (a98d1ce8-3f9c-400e-9027-97bbfd7b41e5) {'id': 'a98d1ce8-3f9c-400e-9027-97bbfd7b41e5', 'created_at': datetime.datetime(2022, 10, 17, 5, 54, 59, 745061), 'updated_at': datetime.datetime(2022, 10, 17, 5, 54, 59, 745076)}"]

(hbnb)create User
95a57602-a569-4deb-b36b-4ccd6a623da2

(hbnb)User.count()
2

(hbnb)BaseModel.count()
1

(hbnb)User.show("a98d1ce8-3f9c-400e-9027-97bbfd7b41e5")
[User] (a98d1ce8-3f9c-400e-9027-97bbfd7b41e5) {'id': 'a98d1ce8-3f9c-400e-9027-97bbfd7b41e5', 'created_at': datetime.datetime(2022, 10, 17, 5, 54, 59, 745061), 'updated_at': datetime.datetime(2022, 10, 17, 5, 54, 59, 745076)}

(hbnb)User.destroy("a98d1ce8-3f9c-400e-9027-97bbfd7b41e5")

(hbnb)User.count()
1

(hbnb)create Place
e6524aa0-b40d-4390-9ab1-aa370a772097

(hbnb)Place.show("e6524aa0-b40d-4390-9ab1-aa370a772097")
[Place] (e6524aa0-b40d-4390-9ab1-aa370a772097) {'id': 'e6524aa0-b40d-4390-9ab1-aa370a772097', 'created_at': datetime.datetime(2022, 10, 17, 6, 9, 34, 95572), 'updated_at': datetime.datetime(2022, 10, 17, 6, 9, 34, 96556)}

(hbnb)Place.update("e6524aa0-b40d-4390-9ab1-aa370a772097", "place_name", "Montevideo")

(hbnb)Place.show("e6524aa0-b40d-4390-9ab1-aa370a772097")
[Place] (e6524aa0-b40d-4390-9ab1-aa370a772097) {'id': 'e6524aa0-b40d-4390-9ab1-aa370a772097', 'created_at': datetime.datetime(2022, 10, 17, 6, 9, 34, 95572), 'updated_at': datetime.datetime(2022, 10, 17, 6, 9, 34, 96556), 'place_name': 'Montevideo'}

</code></pre>  
<h2> File contents </h2>

<table>
<tr>
  <td><strong>Name of file</strong></td>
  <td><strong>Description</strong></td>
</tr>
<tr>
  <td>README.md</td>
  <td>Description of program</td>
</tr>
<tr>
  <td>/models/base_model.py</td>
  <td>BaseModel class: it is the parent class</td>   
</tr>
  
<tr>
  <td>/models/user.py</td>
  <td>User class inherits from BaseModel</td>   
</tr>

<tr>
  <td>/models/state.py</td>
  <td>State class, inherits from BaseModel</td>   
</tr>

<tr>
  <td>/models/city.py</td>
  <td>City class, inherits from BaseModel</td>   
</tr>
  
<tr>
  <td>/models/amenity.py</td>
  <td>Amenity class, inherits from BaseModel</td>   
</tr>

<tr>
  <td>/models/place.py</td>
  <td>Place class, inherits from BaseModel</td>   
</tr>

<tr>
  <td>/models/review.py</td>
  <td>Review class, inherits from BaseModel</td>   
</tr>

<tr>
  <td>/models/engine/file_storage.py</td>
  <td>FileStorage module: contains FileStorage class which has the methods to serializate and deserializate a JSON file</td>
  </tr>
  
  <tr>
  <td>/tests</td>
  <td>This directory contains all unittest to to ensure the performance</td>   
</tr>
  
<tr>
  <td>console.py</td>
  <td>Conmmand interpeter to manage the objects</td>   
</tr>
 
</table>
<br>
<h2> Authors </h2>
Blas Hernández - <a href="https://github.com/blashernandez98"> blashernandez98 </a></p>
Ignacio Martino - <a href="https://github.com/Imartino4"> Imartino4 </a></p>

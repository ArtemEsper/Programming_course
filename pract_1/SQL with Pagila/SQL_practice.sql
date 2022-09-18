/*
1a. You need a list of all the actors’ first name and last name
*/
-- SQL code goes here...

/*
--1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name
*/
-- SQL code goes here...

/*
--2a. You need to find the id, first name, and last name of an actor of whom you know only the first name of "Joe." What is one query would you use to obtain this information?
*/
-- SQL code goes here...

/*
--2b. Find all actors whose last name contain the letters GEN. Make this case insensitive
*/
-- SQL code goes here...

/*
-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order. Make this case insensitive.
*/
-- SQL code goes here...

/*
-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
*/
-- SQL code goes here...

/*
-- 3a. Add a middle_name column to the table actor. Specify the appropriate column type
 */
-- SQL code goes here...


 /*
-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to something that can hold more than varchar.
*/
-- SQL code goes here...


/*
-- 3c. Now write a query that would remove the middle_name column.
*/
-- SQL code goes here...


/*
 -- 4a. List the last names of actors, as well as how many actors have that last name.
*/
 -- SQL code goes here...


/*
-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
*/
-- SQL code goes here...


/*
-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
*/
-- SQL code goes here...


/*
-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
*/
-- SQL code goes here...


/*
-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO(Hint: update the record using a unique identifier.)
 */
-- SQL code goes here...


/*
-- 5a. You’re answering each of these questions. Please include examples and answer them in plain english.
 */
-- SQL code goes here...


/*
-- 6a. Use a JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
*/
-- SQL code goes here...


/*
-- 6b. Use a JOIN to display the total amount rung up by each staff member in January of 2007. Use tables staff and payment.
 */
-- SQL code goes here...


/*
-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
 */
-- SQL code goes here...


/*
-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
 */
-- SQL code goes here...


/*
-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
 */
-- SQL code goes here...


/*
-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. display the titles of movies starting with the letters K and Q whose language is English.
*/
-- SQL code goes here...


/*
-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
*/
-- SQL code goes here...


/*
-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
 */
-- SQL code goes here...


/*
-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as a family film. Now we mentioned family film, but there is no family film category. There’s a category that resembles that. In the real world nothing will be exact.
*/
-- SQL code goes here...


/*
-- 7e. Display the most frequently rented movies in descending order.
 */
-- SQL code goes here...


/*
-- 7f. Write a query to display how much business, in dollars, each store brought in.
 */
-- SQL code goes here...


/*
-- 7g. Write a query to display for each store its store ID, city, and country.
*/
-- SQL code goes here...


/*
-- 7h. List the top five genres in gross revenue in descending order.
 */
-- SQL code goes here...


/*
-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view.
*/
-- SQL code goes here...


/*
-- 8b. How would you display the view that you created in 8a?
*/
-- SQL code goes here...


/*
-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
*/
-- SQL code goes here...



/*
9. Find film category which collects most amount of money during the rent
*/
-- SQL code goes here...



/*
10. Show film titles which are not present in the inventory. Wright query without IN operator.
*/
-- SQL code goes here...


/*
Find top 3 actors, which appear the most in the "Children" category
*/
-- SQL code goes here...


/*
Show the cities with a number of active and not active customers (active customers has customer.active = 1)
Result must be sorted by the number of not active customers in the descending order.
*/
-- SQL code goes here...
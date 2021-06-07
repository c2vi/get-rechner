/*
Fedor, 2021
[!]Only Works if there is a "Pruefen" button
To use it, please find out the name of the entry with: Right Click on the entry -> "untersuchen"/"investigate"
and change the "form" variable
To use copy it in the chrome console and run it (after changing the variables)
*/

var n_try = 100; /*Number of trys the programm should check*/
var sensitivity = 100; /*How sensitive the code should be, (eg for Condensators you may wanna use a lower senitivity as these usually have smaller numbers)*/
var n_steps = 1; /* How much it should add per iteration*/
var starting_nr = 0; /*at what number the bruteforce should start*/
var unit = 'F'; /*what unit the bruteforce will use (adds it at the end of the number)*/
var form = 'questionForm:mcq:1:inpCq';  /*The name of the form that the programm injects the numbers to*/

function sleep(ms) { /* timer function */
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  var i = 0;
  var i2 = 0+starting_nr;
  while (i<n_try) {
      console.log('Iteration:', i);
      document.querySelector('input[name='+form+']').value = String(i2/sensitivity)+unit;
      document.getElementsByName('questionForm:pruefen')[0].click();
      if (0 == 1) { /*ADD CHECKING PART HERE (check if the answer is true then stops goes to the next question*/
          break;
      }
      await sleep(750) /*cant make this shorter bcs letto ping...*/
      i = i+1;
      i2=i2+n_steps;
      }
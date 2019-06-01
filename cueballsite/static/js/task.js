// Initialize Firebase (ADD YOUR OWN DATA)
var config = {
  apiKey: "AIzaSyDnRM1b-dOfkqmaQ94BJyG-0lCo114LPmA",
  authDomain: "reminders-56e2c.firebaseapp.com",
  databaseURL: "https://reminders-56e2c.firebaseio.com",
  projectId: "reminders-56e2c",
  storageBucket: "reminders-56e2c.appspot.com",
  messagingSenderId: "708737581745",
  appId: "1:708737581745:web:4bbba5aeded4f119"
};
firebase.initializeApp(config);

// Reference task collection
var taskRef = firebase.database();

// Listen for form submit
document.getElementsByClassName('NewTaskForm').addEventListener('submit', submitForm);

// Submit form
function submitForm(e){
  e.preventDefault();

  // Get values
  var type = getInputVal('type');
  var name = getInputVal('name');
  var audio = getInputVal('messages');
  var updated = getInputVal('updated');
  var message = getInputVal('message');

  // Save message
  saveTask(type, name, audio, updated, message);
}

// Function to get form  id values
function getInputVal(id){
  return document.getElementById(id).value;
}

// Save message to firebase
function saveTask(type, name, audio, updated, message){
  var newTaskRef = taskRef.push();
  newTaskRef.set({
    name: name,
    name:name,
    audio:audio,
    updated:updated,
    message:message
  });
}
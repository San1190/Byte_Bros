const taskList = document.getElementById("tasks");
const deleteButton = document.querySelectorAll(".button")[0];
const completeButton = document.querySelectorAll(".button")[1];
const addTaskButton = document.getElementById("add");

function addTask() {
    var task = document.getElementById("task").value;
    if (task !== "") {
        var li = document.createElement("li");
        var text = document.createTextNode(task);
        li.appendChild(text);
        taskList.appendChild(li);
        document.getElementById("task").value = "";
    }
}
function addTask2(task) {
    
    if (task !== "") {
        var li = document.createElement("li");
        var text = document.createTextNode(task);
        li.appendChild(text);
        taskList.appendChild(li);
        document.getElementById("task").value = "";
    }
}

function addCompletedTask(task) {
    var completedList = document.getElementById("completed"); // Selecciona la lista de tareas completadas
    if (task !== "") {
        var li = document.createElement("li");
        var text = document.createTextNode(task.textContent); // Obtén el texto de la tarea
        li.appendChild(text);
        completedList.appendChild(li); // Agrega la tarea a la lista de tareas completadas
    }
}

function removeTask() {
    // Eliminar la tarea o tareas seleccionadas
    var tasks = document.querySelectorAll(".marked");
    tasks.forEach(function (task) {
        task.remove();
    });
}

function toggleTaskBackground(event) {
    if (event.target.tagName === "LI") {
        event.target.classList.toggle("marked");
    }
}

document.getElementById("task").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        addTask();
    }
});


//Enviar tarea a completadas
function completeTask() {
    var tasks = document.querySelectorAll(".marked");
    tasks.forEach(function (task) {
        addCompletedTask(task);
        task.remove();
    });
}


function moveTaskBack(event) {
    if (event.target.tagName === "LI") {
        var task = event.target.textContent;
        event.target.remove();

        addTask2(task);
    }
}

document.getElementById("completed").addEventListener('click', moveTaskBack);
addTaskButton.addEventListener("click", addTask);
deleteButton.addEventListener("click", removeTask);
completeButton.addEventListener("click", completeTask);
taskList.addEventListener('click', toggleTaskBackground);



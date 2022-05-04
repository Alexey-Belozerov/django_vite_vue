<template>
  <div class="container">
    <p>
      <label for="new-task">Добавить элемент</label>
      <input @keyup.enter="createTodo" v-model="todoName" id="new-task" type="text" />
      <button @click="createTodo">Добавить</button>
    </p>

    <h3>Список дел</h3>
    <ul id="incomplete-tasks">
      <li v-for="todo in todoList" :key="todo.id">
        <label :class="{ 'line': todo.is_done }">{{ todo.name }}</label>
        <button class="delete" @click="deleteTodo(todo.id)">Удалить</button>
        <button class="edit" @click="doneTodo(todo.id, todo.is_done)">Готово</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onBeforeMount } from 'vue'
const todoList = ref([])
const todoName = ref("")
const doneTodo = (id, bool) => {
  axios.patch(`http://127.0.0.1:8000/api/todo/${id}/`, { "is_done": !bool })
    .then(response => {
      todoList.value.filter((value) => {
        if (id == value.id) {
          value.is_done = !bool
        }
      })
    })
    .catch(error => {
      console.log(error.response)
    })
}
const deleteTodo = (id) => {
  axios.delete(`http://127.0.0.1:8000/api/todo/${id}/`)
    .then(response => {
      todoList.value.filter((value, index) => {
        if (id == value.id) {
          todoList.value.splice(index, 1)
        }
      })
    })
    .catch(error => {
      console.log(error.response)
    })
}
const createTodo = () => {
  if (todoName.value.length == 0) {
    alert("Оставить пустым")
  } else {
    axios.post("http://127.0.0.1:8000/api/todo/", { "name": todoName.value })
      .then(response => {
        todoList.value.push(response.data)
      })
      .catch(error => {
        console.log(error.response)
      })
  }
}
const getTodos = () => {
  axios.get("http://127.0.0.1:8000/api/todo/")
    .then(response => {
      todoList.value = response.data
    })
    .catch(error => {
      console.log(error)
    })
}
onBeforeMount(() => {
  getTodos()
})
</script>



<style>
body {
  background: white url("images/background.jpg") no-repeat;
  background: #D3D3D3;
  color: #333;
  font-family: Roboto, sans-serif;
}
.container {
  display: block;
  width: 400px;
  margin: 50px auto 0;
}
ul {
  margin: 0;
  padding: 0;
}
li * {
  float: left;
}
li,
h3 {
  clear: both;
  list-style: none;
}
input,
button {
  outline: none;
}
button {
  background: none;
  border: 0px;
  color: #241e1e;
  font-size: 15px;
  width: 70px;
  margin: 10px 0 0;
  font-family: Roboto, sans-serif;
  cursor: pointer;
}
button:hover {
  color: #2a3ffa;
}
/* Heading */
h3,
label[for="new-task"] {
  color: #333;
  font-weight: 700;
  font-size: 15px;
  border-bottom: 2px solid #333;
  padding: 30px 0 10px;
  margin: 0;
  text-transform: uppercase;
}
input[type="text"] {
  margin: 0;
  font-size: 18px;
  line-height: 18px;
  height: 18px;
  padding: 10px;
  border: 1px solid #ddd;
  background: #fff;
  border-radius: 6px;
  font-family: Roboto, sans-serif;
  color: #888;
}
input[type="text"]:focus {
  color: #333;
}
/* New Task */
label[for="new-task"] {
  display: block;
  margin: 0 0 20px;
}
input#new-task {
  float: left;
  width: 318px;
}
p > button:hover {
  color: #0fc57c;
}
/* Task list */
li {
  overflow: hidden;
  padding: 20px 0;
  border-bottom: 1px solid #eee;
}
li > input[type="checkbox"] {
  margin: 0 10px;
  position: relative;
  top: 15px;
}
li > label {
  font-size: 18px;
  line-height: 40px;
  width: 237px;
  padding: 0 0 0 11px;
}
li > input[type="text"] {
  width: 226px;
}
li > .delete:hover {
  color: #cf2323;
}
/* Completed */
.line {
  text-decoration: line-through;
  color: #888;
}
/* Edit Task */
ul li input[type="text"] {
  display: none;
}
ul li.editMode input[type="text"] {
  display: block;
}
ul li.editMode label {
  display: none;
}
</style>
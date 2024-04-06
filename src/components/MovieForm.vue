<template>
  <form id="movieForm" @submit.prevent="saveMovie">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" v-model="formData.title" name="title" class="form-control" />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea v-model="formData.description" name="description" class="form-control"></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" @change="handleFileUpload" class="form-control" />
    </div>
    <button type="submit" class="btn btn-primary">Save Movie</button>
    <div v-if="showSuccessMessage" class="alert alert-success mt-3">
      {{ successMessage }}
    </div>
    <div v-if="showErrorMessages" class="alert alert-danger mt-3">
      <ul>
        <li v-for="error in errorMessages" :key="error">{{ error }}</li>
      </ul>
    </div>
  </form>
</template>
<script setup>
import { ref } from "vue";

let csrfToken = ref("");
let showSuccessMessage = ref(false);
let showErrorMessages = ref(false);
let successMessage = ref("");
let errorMessages = ref([]);
let formData = ref({
  title: "",
  description: "",
  poster: null,
});

async function getCsrfToken() {
  try {
    const response = await fetch("/api/v1/csrf-token", {
      headers: {
        Accept: "application/json",
        "User-Agent": "Learning App",
      },
    });
    const data = await response.json();
    csrfToken.value = data.csrf_token;
  } catch (error) {
    console.error("Error fetching CSRF token:", error);
  }
}

async function saveMovie() {
  const movieForm = document.getElementById("movieForm");
  const form_data = new FormData(movieForm);

  // Check if Poster field is valid before adding it to FormData
  if (formData.value.poster) {
    form_data.append("poster", formData.value.poster);
  }

  try {
    const response = await fetch("/api/v1/movies", {
      method: "POST",
      body: form_data,
      headers: {
        "X-CSRFToken": csrfToken.value,
      },
    });

    if (response.ok) {
      const data = await response.json();
      showSuccessMessage.value = true;
      showErrorMessages.value = false;
      successMessage.value = data.message;

      // Clear form data after successful submission
      formData.value.title = "";
      formData.value.description = "";
      formData.value.poster = null;
    } else {
      const errorData = await response.json();
      showSuccessMessage.value = false;
      showErrorMessages.value = true;
      errorMessages.value = errorData.errors;
    }
  } catch (error) {
    console.error("Error in saveMovie:", error);
    showSuccessMessage.value = false;
    showErrorMessages.value = true;
    errorMessages.value = [
      "An unexpected error occurred. Please try again later.",
    ];
  }
}

function handleFileUpload(event) {
  formData.value.poster = event.target.files[0];
}

getCsrfToken();
</script>

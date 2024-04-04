<template>
  <div>
    <form @submit.prevent="saveMovie">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" v-model="movie.title" />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control" rows="4" v-model="movie.description"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster URL</label>
        <input type="text" name="poster" class="form-control" v-model="movie.poster" />
      </div>
      <div class="form-group mb-3">
        <label for="created_at" class="form-label">Created At</label>
        <input type="datetime-local" name="created_at" class="form-control" v-model="movie.created_at" />
      </div>
      <button type="submit" class="btn btn-primary">Save</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      movie: {
        title: '', // Initialize other movie properties here
      },
    };
  },
  methods: {
    saveMovie() {
      // Handle saving movie data here (e.g., send a POST request to the server)
      console.log('Movie saved:', this.movie);

      // Reset form fields after saving
      this.movie = {
        title: '', // Reset other movie properties as needed
      };
    },
  },
};
</script>

<style>
/* Add custom styles for your form if needed */
</style>

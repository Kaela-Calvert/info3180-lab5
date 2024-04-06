<template>
  <div class="container">
    <h1>Movies</h1>
    <div v-if="movies.length === 0" class="no-movies">No movies available</div>
    <div v-else class="gallery-grid">
      <div v-for="movie in movies" :key="movie.id" class="gallery-item">
        <a :href="movie.poster" target="_blank" class="gallery-link">
          <img :src="movie.poster" :alt="movie.title" class="gallery-image" />
        </a>
        <div class="gallery-info">
          <h3 class="gallery-title">{{ movie.title }}</h3>
          <p class="gallery-description">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const movies = ref([]);

async function fetchMovies() {
  try {
    const response = await fetch('/api/v1/movies');
    if (response.ok) {
      const data = await response.json();
      movies.value = data.movies;
    } else {
      console.error('Failed to fetch movies');
    }
  } catch (error) {
    console.error('Error fetching movies:', error);
  }
}

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 20px;
}

.gallery-item {
  background-color: #f1f1f1;
  border-radius: 4px;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.gallery-item:hover {
  transform: scale(1.05);
}

.gallery-link {
  display: block;
}

.gallery-image {
  width: 100%;
  height: 400px;
  object-fit: cover;
}

.gallery-info {
  padding: 15px;
}

.gallery-title {
  margin-top: 0;
  margin-bottom: 5px;
  font-size: 1.2rem;
}

.gallery-description {
  margin: 0;
  font-size: 0.9rem;
  color: #666;
}

.no-movies {
  text-align: center;
  font-size: 1.2rem;
  color: #888;
  margin-top: 40px;
}
</style>
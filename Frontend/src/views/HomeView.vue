<template>
  <div class="home-container">
    <transition name="fade-slide">
      <div class="home-content" v-if="showContent">
        <img src="../assets/maze-logo.svg" alt="Logo Maze-Droner" class="home-image">
        <h1 class="title">Bienvenido a Maze-Droner</h1>
        <p class="subtitle">¡Demostr&aacute; tus reflejos y gui&aacute; al dron hacia el final!</p>

        <div class="instructions-box">
          <h2>Instrucciones del juego</h2>
          <ul>
            <li>1. <strong>Ingresa</strong> tu nombre de jugador.</li>
            <li>2. Click en <strong>"Comenzar"</strong> para empezar el tiempo.</li>
            <li>3. Usa las <strong>flechas</strong> para mover el dron por el laberinto.</li>
            <li>4. Encuentra la salida rapidamente.</li>
            <li>5. Al salir del laberinto deten rapidamente el tiempo.</li>
            <li>6. Tu tiempo se guardará automáticamente al terminar la partida.</li>
          </ul>
        </div>

        <div class="tips-box">
          <h2>Consejos</h2>
          <p>
            Planificá tus movimientos, prestá atención al entorno y tratá de completar el laberinto en el menor tiempo posible.
          </p>
        </div>

        <transition name="pop">
          <button class="start-btn" @click="goToPlay" v-if="showContent">
            Comenzar Juego
          </button>
        </transition>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const showContent = ref(false);

onMounted(() => {
  setTimeout(() => (showContent.value = true), 300);
});

const goToPlay = () => {
  router.push("/play");
};
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  background: linear-gradient(135deg, #00a6e826, #0076b636);
  font-family: "Poppins", sans-serif;
  overflow: hidden;
}

.home-content {
  max-width: 700px;
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(10px);
  border-radius: 1.5rem;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: 2.5rem;
  box-shadow: 0 0 25px rgba(0, 0, 0, 0.4);
  animation: floatIn 1s ease;
}

.home-image {
  width: 80px;
  height: 80px;
  object-fit: contain;
  animation: floatImage 3s ease-in-out infinite;
  filter: drop-shadow(0 0 15px rgb(99, 99, 99));
}

.title {
  font-size: 2.2rem;
  margin-bottom: 0.6rem;
  color: #00d1ff;
  background-color: #1e1e1e;
  border-radius: 20px;
  padding: 15px;
  margin-left: 10%;
  margin-right: 10%;
}

.subtitle {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.instructions-box,
.tips-box {
  text-align: left;
  margin: 1.5rem 0;
  padding: 1.5rem;
  border-radius: 1rem;
  background: #1e1e1e;
  box-shadow: 0 0 10px rgb(99, 99, 99);
  transition: transform 0.3s ease;
}

.instructions-box:hover,
.tips-box:hover {
  transform: scale(1.03);
}

.instructions-box h2,
.tips-box h2 {
  color: #00d1ff;
  margin-bottom: 1rem;
}

.instructions-box ul,
.tips-box p {
  color: #fff;
  list-style: none;
  padding: 0;
}

.instructions-box li {
  margin: 0.6rem 0;
  font-size: 1rem;
  line-height: 1.5;
}

.start-btn {
  margin-top: 2rem;
  padding: 0.9rem 2rem;
  font-size: 1.1rem;
  font-weight: bold;
  color: #fff;
  background: linear-gradient(135deg, #00d1ff, #0078ff);
  border: none;
  border-radius: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 0 15px rgba(0, 209, 255, 0.4);
}

.start-btn:hover {
  transform: scale(1.08);
  box-shadow: 0 0 25px rgba(0, 209, 255, 0.7);
}

/* Animaciones globales coherentes */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.6s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.pop-enter-active,
.pop-leave-active {
  transition: all 0.35s ease;
}
.pop-enter-from,
.pop-leave-to {
  transform: scale(0.8);
  opacity: 0;
}

@keyframes floatIn {
  from {
    transform: scale(0.9);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
</style>

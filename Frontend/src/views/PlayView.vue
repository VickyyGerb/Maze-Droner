<template>
  <div class="play-container">
    <!-- Nombre de usuario -->
    <div v-if="!usernameSaved" class="username-box">
      <h2>Ingresá tu nombre de jugador</h2>
      <input v-model="username" type="text" placeholder="Tu nombre" />
      <button @click="saveUsername" :disabled="!username">Guardar</button>
    </div>

    <!-- Zona de juego -->
    <div v-else class="game-layout">
      <!-- Columna izquierda -->
      <div class="left-column">
        <h2 class="player-name">Jugador: {{ username }}</h2>
        <div class="timer">{{ formattedTime }}</div>

        <div class="controls">
          <button v-if="!isPlaying" class="start" @click="startGame">Comenzar</button>
          <button v-else class="stop" @click="stopGame">Detener</button>
        </div>
      </div>

      <!-- Columna derecha -->
      <div class="right-column">
        <div class="joystick">
          <button class="arrow up" @click="handleMove('arriba')">▲</button>
          <div class="middle-row">
            <button class="arrow left" @click="handleMove('izquierda')">◀</button>
            <button class="arrow right" @click="handleMove('derecha')">▶</button>
          </div>
          <button class="arrow down" @click="handleMove('abajo')">▼</button>
        </div>
      </div>
    </div>

    <!-- Mensaje si intenta mover sin comenzar -->
    <div v-if="message" class="alert">{{ message }}</div>

    <!-- 🪟 Modal de resultado -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <h2>¡Juego finalizado!</h2>
        <p>Tu tiempo fue de <strong>{{ formattedTime }}</strong></p>
        <div class="modal-buttons">
          <button class="close" @click="closeModal">Cerrar</button>
          <button class="ranking" @click="goToRanking">Ver Ranking</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const username = ref('')
const usernameSaved = ref(false)
const time = ref(0)
const isPlaying = ref(false)
const timerInterval = ref(null)
const message = ref('')
const showModal = ref(false)

const formattedTime = computed(() => {
  const minutes = Math.floor(time.value / 60)
  const seconds = time.value % 60
  return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
})

function saveUsername() {
  usernameSaved.value = true
}

function startGame() {
  if (isPlaying.value) return
  isPlaying.value = true
  message.value = ''
  time.value = 0

  timerInterval.value = setInterval(() => {
    time.value++
  }, 1000)
}

function stopGame() {
  isPlaying.value = false
  clearInterval(timerInterval.value)

  const results = JSON.parse(localStorage.getItem('ranking') || '[]')
  results.push({ name: username.value, time: time.value })
  localStorage.setItem('ranking', JSON.stringify(results))

  showModal.value = true
}

function handleMove() {
  if (!isPlaying.value) {
    message.value = 'Primero debés comenzar el juego'
    return
  }
}

function closeModal() {
  showModal.value = false
}

function goToRanking() {
  showModal.value = false
  router.push('/ranking')
}

onUnmounted(() => clearInterval(timerInterval.value))
</script>

<style scoped>
.play-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  background: linear-gradient(135deg, #00a6e826, #0076b636);
  font-family: "Poppins", sans-serif;
  overflow: hidden;
}

.game-layout {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 150px;
  width: 100%;
  height: 100%;
  animation: fadeIn 0.5s ease;
}

.left-column,
.right-column {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.username-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  margin: 50px;
  font-size: 22px;
  padding: 40px 60px;
  background-color: #1e1e1e;
  border-radius: 20px;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(6px);
  animation: fadeIn 0.5s ease;
}

.username-box h2 {
  font-size: 26px;
  margin-bottom: 8px;
  font-weight: 600;
  color: #ffffff;
}

.username-box input {
  padding: 12px 20px;
  font-size: 20px;
  border-radius: 10px;
  margin-bottom: 10px;
  border: none;
  outline: none;
  width: 280px;
  text-align: center;
  background: rgba(255, 255, 255, 0.85);
  transition: all 0.3s;
}

.username-box input:focus {
  transform: scale(1.03);
  box-shadow: 0 0 8px #00b4d8;
}

.username-box button {
  padding: 12px 30px;
  font-size: 18px;
  font-weight: 600;
  background: linear-gradient(90deg, #00b4d8, #0077b6);
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
}

.username-box button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.5);
}

.player-name {
  font-size: 26px;
  font-weight: 600;
  color: #1e1e1e;
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.1);
  animation: fadeIn 0.5s ease;
}

.timer {
  padding: 20px;
  font-size: 80px;
  font-weight: 700;
  background-color: #1e1e1e;
  border-radius: 50px;
  color: #ffffff;
  text-shadow: 0 0 12px rgba(231, 231, 231, 0.6);
}

.controls {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.controls button {
  padding: 15px 45px;
  margin-top: 30px;
  font-size: 20px;
  border-radius: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.controls .start {
  background: linear-gradient(90deg, #4caf50, #2e7d32);
  color: white;
}

.controls .start:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.6);
}

.controls .stop {
  background: linear-gradient(90deg, #f44336, #c62828);
  color: white;
}

.controls .stop:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 6px 20px rgba(244, 67, 54, 0.6);
}

.joystick {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  margin-top: 35px;
  padding: 35px;
  border-radius: 25px;
  backdrop-filter: blur(4px);
  animation: fadeIn 0.5s ease;
}

.middle-row {
  display: flex;
  gap: 100px;
}

.arrow {
  width: 95px;
  height: 95px;
  font-size: 40px;
  font-weight: bold;
  border: none;
  background: radial-gradient(circle, #1e1e1e 60%, #111);
  color: #fff;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.2s;
}

.arrow:hover {
  background: radial-gradient(circle, #2a2a2a 60%, #000);
  transform: scale(1.08);
  box-shadow: 0 0 15px #474747;
}

.alert {
  background: linear-gradient(135deg, #ff4e4e, #d32f2f);
  color: #ffffff;
  border-radius: 10px;
  padding: 15px 25px;
  font-size: 18px;
  margin-top: 25px;
  text-align: center;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(3px);
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.75);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
  animation: fadeIn 0.4s ease;
}

.modal-content {
  background: linear-gradient(180deg, #ffffff, #e6f7ff);
  padding: 45px 70px;
  border-radius: 25px;
  text-align: center;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
  animation: popUp 0.4s ease;
}

.modal-content h2 {
  font-size: 34px;
  color: #0077b6;
  margin-bottom: 20px;
}

.modal-content p {
  font-size: 22px;
  margin-bottom: 35px;
  color: #333;
}

.modal-buttons {
  display: flex;
  justify-content: center;
  gap: 25px;
}

.modal-buttons button {
  padding: 12px 32px;
  font-size: 18px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 600;
}

.modal-buttons .close {
  background: linear-gradient(135deg, #6c757d, #495057);
  color: white;
  padding: 14px 35px;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.25s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
}

.modal-buttons .close:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px #6c757d;
}

.modal-buttons .ranking {
  background: linear-gradient(90deg, #00b4d8, #0077b6);
  color: white;
}

.modal-buttons .ranking:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px #00b4d8;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes popUp {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes pulse {
  0%, 100% {
    text-shadow: 0 0 10px rgba(0, 224, 255, 0.6);
  }
  50% {
    text-shadow: 0 0 25px rgba(0, 224, 255, 0.9);
  }
}
</style>

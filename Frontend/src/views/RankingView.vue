<template>
  <div class="ranking-container">
    <h2>Ranking de Jugadores</h2>

    <table v-if="ranking.length" class="ranking-table">
      <thead>
        <tr>
          <th>Posición</th>
          <th>Nombre</th>
          <th>Tiempo</th>
          <th>Acción</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(player, index) in sortedRanking" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ player.name }}</td>
          <td>{{ formatTime(player.time) }}</td>
          <td>
            <button class="delete-btn" @click="removePlayer(index)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else class="empty">Aún no hay jugadores registrados.</p>

    <div class="buttons">
      <button class="clear-all" @click="showModal = true" v-if="ranking.length">
        Eliminar todo
      </button>
      <button class="back" @click="goBack">Volver</button>
    </div>

    <!-- Modal de confirmación -->
    <transition name="fade">
      <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
        <transition name="pop">
          <div v-if="showModal" class="modal-content">
            <h3>¿Estás seguro?</h3>
            <p>Esto eliminará <strong>todos</strong> los registros del ranking.</p>
            <div class="modal-buttons">
              <button class="confirm-btn" @click="confirmClearAll">Sí, eliminar</button>
              <button class="cancel-btn" @click="showModal = false">Cancelar</button>
            </div>
          </div>
        </transition>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const ranking = ref([])
const showModal = ref(false)

onMounted(() => {
  const data = JSON.parse(localStorage.getItem('ranking') || '[]')
  ranking.value = data
})

const sortedRanking = computed(() =>
  [...ranking.value].sort((a, b) => a.time - b.time)
)

function formatTime(seconds) {
  const min = Math.floor(seconds / 60)
  const sec = seconds % 60
  return `${String(min).padStart(2, '0')}:${String(sec).padStart(2, '0')}`
}

function removePlayer(index) {
  ranking.value.splice(index, 1)
  localStorage.setItem('ranking', JSON.stringify(ranking.value))
}

function confirmClearAll() {
  ranking.value = []
  localStorage.removeItem('ranking')
  showModal.value = false
}

function goBack() {
  router.push('/play')
}
</script>

<style scoped>
/* ====== Base ====== */
.ranking-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  background: linear-gradient(135deg, #00a6e826, #0076b636);
  font-family: "Poppins", sans-serif;
  overflow: hidden;
}

h2 {
  font-size: 36px;
  color: #222;
  font-weight: 700;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

/* ====== Tabla ====== */
.ranking-table {
  width: 80%;
  border-collapse: collapse;
  background-color: #ffffff;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  border-radius: 14px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.ranking-table th,
.ranking-table td {
  padding: 16px 20px;
  text-align: center;
  border-bottom: 1px solid #e0e0e0;
  font-size: 18px;
}

.ranking-table th {
  background: linear-gradient(135deg, #00a8e8, #0077b6);
  color: #fff;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.ranking-table tr:hover {
  background-color: #ffffff;
  transform: scale(1.01);
}

/* ====== Botones ====== */
.delete-btn {
  background: linear-gradient(135deg, #ff4e4e, #d32f2f);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.25s ease;
  font-weight: 1000;
  box-shadow: 0 3px 6px rgba(255, 76, 76, 0.3);
}

.delete-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 12px rgba(255, 76, 76, 0.5);
}

.delete-btn:active {
  transform: scale(0.95);
}

.buttons {
  display: flex;
  gap: 25px;
  margin-top: 40px;
  margin-bottom: 40px;
}

.clear-all {
  background: linear-gradient(135deg, #ff4e4e, #d32f2f);
  color: white;
  padding: 14px 35px;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.25s ease;
  box-shadow: 0 4px 10px rgba(255, 122, 0, 0.3);
}

.clear-all:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 14px rgba(255, 122, 0, 0.5);
}

.clear-all:active {
  transform: scale(0.96);
}

.back {
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

.back:hover {
  background: linear-gradient(135deg, #495057, #343a40);
  transform: translateY(-2px);
}

.back:active {
  transform: scale(0.96);
}

.empty {
  font-size: 22px;
  color: #444;
  margin-top: 20px;
  font-weight: 500;
}

/* ====== Modal ====== */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 50;
  backdrop-filter: blur(3px);
}

.modal-content {
  background: #fff;
  text-align: center;
  padding: 35px 45px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  max-width: 400px;
  width: 90%;
  transform: scale(1);
}

.modal-content h3 {
  font-size: 26px;
  color: #222;
  font-weight: 700;
  margin-bottom: 10px;
}

.modal-content p {
  font-size: 18px;
  color: #555;
  margin-bottom: 25px;

}

.modal-buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.confirm-btn {
  background: linear-gradient(135deg, #ff4e4e, #d32f2f);
  color: white;
  padding: 10px 25px;
  border: none;
  border-radius: 10px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.25s ease;
}

.confirm-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 12px rgba(255, 76, 76, 0.5);
}

.cancel-btn {
  background: linear-gradient(135deg, #6c757d, #495057);
  color: white;
  padding: 10px 25px;
  border: none;
  border-radius: 10px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.25s ease;
}

.cancel-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 12px rgba(0, 0, 0, 0.25);
}

/* ====== Animaciones ====== */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.pop-enter-active {
  transition: all 0.3s cubic-bezier(0.18, 0.89, 0.32, 1.28);
}
.pop-enter-from {
  transform: scale(0.7);
  opacity: 0;
}
.pop-leave-active {
  transition: all 0.2s ease;
  transform: scale(0.8);
  opacity: 0;
}
</style>

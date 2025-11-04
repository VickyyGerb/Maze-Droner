<template>
  <header class="header">
    <nav class="nav-bar">
      <h2 class="logo">Maze-Droner</h2>
      <ul class="nav-links">
        <li><router-link to="/">Inicio</router-link></li>
        <li><router-link to="/play">Jugar</router-link></li>
        <li><router-link to="/ranking">Ranking</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
.header {
  background-color: #1e1e1e;
  color: white;
  padding: 15px 40px;
  box-shadow: 0 0 12px rgba(0, 209, 255, 0.25);
}

.nav-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1100px;
  margin: 0 auto;
}

.logo {
  font-size: 1.8rem;
  font-weight: 700;
  color: #00d1ff;
  letter-spacing: 1px;
  text-shadow: 0 0 10px rgba(0, 209, 255, 0.6);
}

.nav-links {
  display: flex;
  gap: 30px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem;
  transition: all 0.25s ease;
  position: relative;
}

.nav-links a::after {
  content: "";
  position: absolute;
  width: 0%;
  height: 2px;
  bottom: -4px;
  left: 0;
  background-color: #00d1ff;
  transition: width 0.3s ease;
}

.nav-links a:hover::after {
  width: 100%;
}

.nav-links a.router-link-exact-active {
  color: #00d1ff;
}
.nav-links a.router-link-exact-active::after {
  width: 100%;
}

/* Animación suave del título */
@keyframes glowPulse {
  0% {
    text-shadow: 0 0 6px rgba(0, 209, 255, 0.5);
  }
  50% {
    text-shadow: 0 0 16px rgba(0, 209, 255, 1);
  }
  100% {
    text-shadow: 0 0 6px rgba(0, 209, 255, 0.5);
  }
}
</style>

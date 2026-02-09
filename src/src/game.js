// src/game.js – wird von index.html geladen
let gameData = {};

async function loadGame() {
  const res = await fetch('charismata_data.json');
  gameData = await res.json();
  renderGifts();
  updatePlayerStats();
}

function activateGift(id) {
  const gift = gameData.charismata.find(g => g.id === id);
  if (!gift) return;
  
  gift.stats.daily_activations++;
  gameData.player.total_grace += gift.stats.grace_bonus;
  
  // Level-up Logik (einfach)
  gameData.player.level = Math.floor(gameData.player.total_grace / 100) + 1;
  
  localStorage.setItem('charismaGame', JSON.stringify(gameData));
  renderGifts();
  updatePlayerStats();
  
  alert(`✨ ${gift.name_de} aktiviert! +${gift.stats.grace_bonus} Grace`);
}

function renderGifts() {
  // ... (kann in index.html erweitert werden, siehe unten)
}

function updatePlayerStats() {
  document.getElementById('total-grace').textContent = gameData.player.total_grace;
  document.getElementById('player-level').textContent = gameData.player.level;
}

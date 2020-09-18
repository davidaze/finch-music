import React, { useState } from 'react';
import './App.css';
import { getGenre } from './api'

function App() {
  const [lyric, setLyric] = useState('')
  const [genre, setGenre] = useState(null)
  async function handleSubmit() {
    try {
      const responseGenre = await getGenre(lyric)
      if (responseGenre) {
        setGenre(responseGenre)
      }
    } catch (e) {
      alert(e.message)
    }
  }
  if (genre) {
    return (
      <div className="App">
        <h1>Preditor de Gênero Musical</h1>

        <h2>O gênero da música é: <p>{genre}</p></h2>

        <button onClick={() => { setGenre(null) }}>Voltar</button>
      </div>
    )
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>Preditor de Gênero Musical</h1>
        <h3>Gêneros suportados: Bossa Nova, Funk, Gospel e Sertanejo</h3>
      </header>
      <div className='form' onSubmit={handleSubmit}>
        <textarea placeholder='Insira a letra da música aqui' value={lyric} onChange={e => setLyric(e.target.value)} ></textarea>
        <button onClick={() => { handleSubmit() }}>Enviar</button>
      </div>
    </div>
  );
}

export default App;

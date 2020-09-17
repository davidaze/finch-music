import React from 'react';
import './App.css';

function App() {
  function handleSubmit(data) {
    console.log(data)
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>Preditor de Gênero</h1>
        <h3>Gêneros suportados: Bossa Nova, Funk, Gospel e Sertanejo</h3>
        <form onSubmit={handleSubmit}>
          <textarea placeholder='Insira a letra da música aqui'></textarea>
          <button type={'submit'}>Enviar</button>
        </form>
      </header>
    </div>
  );
}

export default App;

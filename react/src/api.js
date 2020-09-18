const baseurl = 'http://localhost:5000/'
export async function getGenre(lyric) {
  try {
    const response = await fetch(baseurl + 'model/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        lyric
      })
    })
    const data = await response.json()
    if (response.ok) return data.genre
    else alert('Ops! Algo deu errado')
    return null
  } catch (e) {
    alert(e.message)
  }
}
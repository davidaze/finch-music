const baseurl = 'https://finch-music-backend.herokuapp.com/'
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
    if (response.status === 401) alert('Ops! Isso é uma letra de música?')
    else 
    return null
  } catch (e) {
    alert(e.message)
  }
}
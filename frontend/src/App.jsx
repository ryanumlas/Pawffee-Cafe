import background1 from './assets/background1.png'
import happy_bunny from './assets/bunny/happy_bunny.png'

function App() {
  return (
    <div
      className="min-h-screen bg-cover bg-center"
      style={{
        backgroundImage: `url(${background1})`,
      }}
    >
    </div>
  )
}

export default App
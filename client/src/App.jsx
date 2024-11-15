import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import Siva from './components/Siva';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
<Siva/>
    </>
  )
}

export default App

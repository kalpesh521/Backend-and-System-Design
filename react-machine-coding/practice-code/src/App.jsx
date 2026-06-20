import { useState } from 'react' 
import './App.css'
import Otp from './components/Otp'
import ToastContainer from './components/ToastContainer'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <Otp /> */}
      <ToastContainer />
    </>
  )
}

export default App

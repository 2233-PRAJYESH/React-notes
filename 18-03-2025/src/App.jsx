import { Routes, Route } from 'react-router-dom';

import './App.css'
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Clothes from './pages/Clothes';
import { useEffect } from 'react';
import Employees from './pages/Employees';
import Groceries from './pages/Groceries';
import ClothDetails from './pages/ClothDetails';
import UserList from './pages/UserList';

function App() {

  useEffect(() => {
    console.log('In use effect1 function...');
  }, []);

  useEffect(() => {
    console.log('In use effect2 function...');
  }, []);

  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/clothes" element={<Clothes />}></Route>
        <Route path="/cloth-details/:id" element={<ClothDetails />}></Route>
        <Route path="/employees" element={<Employees />}></Route>
        <Route path="/groceries" element={<Groceries />}></Route>
        <Route path="/user-list" element={<UserList />}></Route>
      </Routes>
      {/* <Home/>
      <Clothes/>
      <Employees/>
      <Groceries/> */}
      <Footer />
    </div>
  )
}

export default App

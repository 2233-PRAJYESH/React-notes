import { Routes, Route } from 'react-router-dom';
import { lazy, Suspense } from 'react';

import './App.css'
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Clothes from './pages/Clothes';
import { useEffect } from 'react';
// import Employees from './pages/Employees';
const Employees = lazy(() => import('./pages/Employees'));
import Groceries from './pages/Groceries';
import ClothDetails from './pages/ClothDetails';
import UserList from './pages/UserList';
import Register from './pages/Register';
import Cart from './pages/Cart';
import Loader from './components/Loader';

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
      <Suspense fallback={<Loader/>}>
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/clothes" element={<Clothes />}></Route>
          <Route path="/cloth-details/:id" element={<ClothDetails />}></Route>
          <Route path="/employees" element={<Employees />}></Route>
          <Route path="/groceries" element={<Groceries />}></Route>
          <Route path="/user-list" element={<UserList />}></Route>
          <Route path="/register" element={<Register/>}></Route>
          <Route path="/cart" element={<Cart/>}></Route>
        </Routes>
      </Suspense>
      <Footer />
    </div>
  )
}

export default App

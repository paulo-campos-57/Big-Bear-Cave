import { Routes, Route } from "react-router-dom";
import Index from "./pages/Index";
import Cadastro from "./pages/Cadastro";

export default function App() {
  return(
    <>
      <Routes>
        <Route path="/" element={<Index />}/>
        <Route path="/cadastro" element={<Cadastro />} />
      </Routes>
    </>
  );
}
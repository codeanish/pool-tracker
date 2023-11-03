import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Player from "./pages/Player";

const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigate to="/player"/>}/>
                <Route path="/player" element={<Player/>}/>
            </Routes>
        </BrowserRouter>
    )
};

export default Router;

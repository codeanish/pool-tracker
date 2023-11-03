import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import PlayerPage from "./pages/PlayerPage";

const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigate to="/player"/>}/>
                <Route path="/player" element={<PlayerPage/>}/>
            </Routes>
        </BrowserRouter>
    )
};

export default Router;

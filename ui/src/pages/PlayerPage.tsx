import { useEffect, useState } from "react";
import PageHeader from "../components/PageHeader";
import Player from "../types/Player";
import { useNavigate, useParams } from "react-router-dom";
import PlayerService from "../services/PlayerService";

const PlayerPage = () => {

    const [player, setPlayer] = useState<Player>({
        name: '',
        email: '',
    });
    
    // type CardParams = {
    //     username: string;
    // }
    // const { username } = useParams<CardParams>();
    // const navigate = useNavigate();

    useEffect(() => {
        fetchPlayer();
    },[]);

    const fetchPlayer = async () => {
        PlayerService.getPlayer(1).then((data) => {
            setPlayer(data);
        })
    };

    return (
        <>
        <PageHeader/>
        <div className="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8 sm:py-6 lg:py-8">
            <h1>{player.name}</h1>
        </div>
        </>
    )
};

export default PlayerPage;
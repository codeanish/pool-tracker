import { useEffect, useState } from "react";
import PageHeader from "../components/PageHeader";
import Player from "../types/Player";
import PlayerService from "../services/PlayerService";

const PlayerPage = () => {

    const [player, setPlayer] = useState<Player>({
        name: '',
        email: '',
    });

    useEffect(() => {
        fetchPlayer();
    }, []);

    const fetchPlayer = async () => {
        console.log("fetchPlayer");
        PlayerService.getPlayer(6).then((data) => {
            setPlayer(data);
        })
    };

    return (
        <>
            <PageHeader />
            <div className="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8 sm:py-6 lg:py-8">
                <h1>{player.name}</h1>
            </div>
        </>
    )
};

export default PlayerPage;

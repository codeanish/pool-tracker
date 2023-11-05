import axios from 'axios';
import Player from '../types/Player';

const baseUrl = 'http://localhost:8000/players';

const getPlayer = async (id: number): Promise<Player> => {
    const response = await axios.get(`${baseUrl}/${id}`);
    return response.data;
}

const PlayerService = {
    getPlayer
}

export default PlayerService;
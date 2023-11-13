import axios from 'axios';
import Player from '../types/Player';
import pooltrackerConfig from '../config';

const baseUrl = pooltrackerConfig.baseUrl;


const getPlayer = async (id: number): Promise<Player> => {
    const response = await axios.get(`${baseUrl}/players/${id}`);
    return response.data;
}

const PlayerService = {
    getPlayer
}

export default PlayerService;

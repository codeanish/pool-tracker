import axios from 'axios';
import Player from '../types/Player';

var baseUrl = import.meta.env.API_URL
console.log(baseUrl)


const getPlayer = async (id: number): Promise<Player> => {
    const response = await axios.get(`${baseUrl}/${id}`);
    return response.data;
}

const PlayerService = {
    getPlayer
}

export default PlayerService;

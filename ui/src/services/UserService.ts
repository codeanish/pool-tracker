import axios from 'axios';
import Player from '../types/Player';

const baseUrl = '/api/players';

const getUser = async (id: string): Promise<Player> => {
    const response = await axios.get(`${baseUrl}/${id}`);
    return response.data;
}

const UserService = {
    getUser
}

export default UserService;
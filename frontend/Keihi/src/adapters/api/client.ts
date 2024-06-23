import axios from 'axios';

export const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
});

export const fetchHealth = async () => {
  try {
    const response = await apiClient.get('/test');
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar dados do backend:', error);
    throw error;
  }
};
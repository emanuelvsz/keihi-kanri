import axios from 'axios';
import { StatusBar } from 'expo-status-bar';
import { useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import HealthScreen from './src/ui/screens/health';

export default function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/test')
      .then(response => {
        setMessage('Resposta do servidor: ' + response.data);
      })
      .catch(error => {
        setMessage('Erro ao buscar dados do backend');
      });
  }, []);

  return (
    <HealthScreen />
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

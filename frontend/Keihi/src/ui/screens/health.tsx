import React, { useEffect, useState } from 'react';
import { StyleSheet, View } from 'react-native';
import { fetchHealthMessage } from '../../domain/useCases/health';
import HealthComponent from '../components/health';
import { HealthModel } from '../../domain/models/health';

const HealthScreen = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const loadMessage = async () => {
      try {
        const testMessage = await fetchHealthMessage();
        setMessage(testMessage.message);
      } catch (error) {
        setMessage('Erro ao buscar dados do backend');
      }
    };

    loadMessage();
  }, []);

  return (
    <View style={styles.container}>
      <HealthComponent message={new HealthModel(message)} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default HealthScreen;

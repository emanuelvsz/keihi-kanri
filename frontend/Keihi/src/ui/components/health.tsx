// src/presentation/components/TestComponent.js

import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { HealthModel } from '../../domain/models/health';

interface HealthComponentProps {
    message: HealthModel;
  }

const HealthComponent = ({ message }: HealthComponentProps) => {
  return (
    <View style={styles.container}>
      <Text>{message.message}</Text>
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

export default HealthComponent;

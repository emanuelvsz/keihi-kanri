import HealthScreen from './src/ui/screens/health';

import { StyleSheet} from 'react-native';

export default function App() {
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

import { StyleSheet} from 'react-native';
import HealthScreen from './src/ui/screens/health';

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

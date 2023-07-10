import * as React from 'react';
import { View, Text,Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import VentanaTest  from './Lista';
import Barcode from './Barcode';
import Camara from './camara';
import ImagePickerExample from './assets/Verimagen';
function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Pantalla principal</Text>
      <Button
        title="Ir a lista"
        onPress={() => navigation.navigate('Lista')}
      />
    </View>
  );
}

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Inicio">
        <Stack.Screen name="Inicio" component={HomeScreen} />
        <Stack.Screen name="Picker" component={ImagePickerExample} />
        <Stack.Screen name="Lista" component={VentanaTest} />
        <Stack.Screen name="Barcode" component={Barcode} />
        <Stack.Screen name="Camera" component={Camara} />

      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
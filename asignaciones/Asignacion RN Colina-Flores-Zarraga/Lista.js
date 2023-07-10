import React from 'react';
import {
  SafeAreaView,
  View,
  FlatList,
  StyleSheet,
  Text,
  StatusBar,
  Pressable
} from 'react-native';

const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'Escaner de QR',
    detalle:'Barcode'
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Seleccionar imagen',
    detalle:'Picker'

  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Cámara',
    detalle:'Camera'
  }
];


export function Lista({navigation})  {
const Item = ({title, detalle}) => (
    <Pressable
        onPress={() => navigation.navigate(detalle)}
        style={({pressed}) => [
            {
                backgroundColor: pressed ? 'rgb(210, 230, 255)' : 'white',
            },
            styles.wrapperCustom,
        ]}
    >
        <View style={styles.item}>
            <Text style={styles.title}>{title}</Text>
            <Text style={styles.title}>detalle: {detalle}</Text>
        </View>
    </Pressable>
);
  return (
    <SafeAreaView style={styles.container}>
      <FlatList
        data={DATA}
        renderItem={({item}) => <Item title={item.title} detalle={item.detalle}/>}
        keyExtractor={item => item.id}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: StatusBar.currentHeight || 0,
  },
  item: {
    backgroundColor: '#f9c666',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
    marginTop:10
  },
  title: {
    fontSize: 32,
  },
});

export default Lista;
import { Text, StyleSheet, View } from 'react-native'
import React from 'react';
import Downmenu from '../components/downmenu';

export default function Homepage() {
    return(
        <View style={styles.home}>
            <Text>in homepage</Text>
            <Downmenu/>

        </View>
    );
}

const styles = StyleSheet.create({
    home:{
        flex:1,
        padding:10
    }
})

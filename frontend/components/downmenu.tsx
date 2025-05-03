import { Text, StyleSheet, View, TouchableOpacity, Image } from 'react-native'
import { useRouter } from 'expo-router';

export default function Downmenu() {
    const router = useRouter()
    return (
        <View style={styles.rectangleIcon}>
            <View style={styles.inFlex}>
                <View style={styles.ineach}>
                    <TouchableOpacity onPress={() => router.push('/homepage')}>
                        <Image style={styles.imgset} source={require("../assets/images/user.png")} />
                        <Text style={styles.tex}>Profile</Text>
                    </TouchableOpacity>
                </View>
                <View style={styles.ineach}>
                    <TouchableOpacity onPress={() => router.push('/homepage')}>
                        <Image style={styles.imgset} source={require("../assets/images/medicine.png")} />
                        <Text style={styles.tex}>Check</Text>
                    </TouchableOpacity>
                </View>
                <View style={styles.ineach}>
                    <TouchableOpacity onPress={() => router.push('/chatbot')}>
                        <Image style={styles.imgset} source={require("../assets/images/chat.png")} />
                        <Text style={styles.tex}>Chat-Bot</Text>
                    </TouchableOpacity>
                </View>
                <View style={styles.ineach}>
                    <TouchableOpacity onPress={() => router.push('/chatbot')}>
                        <Image style={styles.imgset} source={require("../assets/images/calendar.png")} />
                        <Text style={styles.tex}>Calandar</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </View>
    );
}
const styles = StyleSheet.create({
    rectangleIcon: {
        borderRadius: 7,
        height: 90,
        backgroundColor: "rgba(92, 167, 136, 0.84)"
    },
    inFlex: {
        padding: 15,
        gap: 65,
        flexDirection: 'row',
        alignItems: 'center',
    },
    imgset: {
        height: 51
    },
    ineach: {
        alignContent: "center",
    },
    tex:{
        fontSize: 15,
        fontWeight: "600",
        fontFamily: "MontaguSlab144pt-SemiBold",
        color: "#fff",
    }

})

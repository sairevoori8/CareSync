import * as React from "react";
import { Text, StyleSheet, Image, View, TextInput, TouchableOpacity } from "react-native";
import { useRouter } from 'expo-router';

const Frame = () => {
	const [user, userTxt] = React.useState("");
	const [pass, usePass] = React.useState("");
	const router = useRouter()

	return (
		<View style={[styles.caresyncParent]}>
			<View style={styles.spacer1}></View>
			<Text style={styles.caresync}>CareSync</Text>
			<Text style={styles.connectingHealthcareSeamless}>Connecting healthcare seamlessly.</Text>
			<View style={styles.spacer2}></View>
			<View style={styles.inpcon}>
				<View style={[styles.eachIn, styles.bodCk]}>
					<Image style={styles.Imgset} source={require("../assets/images/usericn.png")} />
					<TextInput
						style={styles.txt}
						onChangeText={userTxt}
						value={user}
						placeholder="Username"
					/>
				</View>
				<View style={[styles.eachIn, styles.bodCk]}>
					<Image style={styles.Imgset} source={require("../assets/images/passicn.png")} />
					<TextInput
						style={styles.txt}
						onChangeText={usePass}
						value={pass}
						placeholder="Password"
					/>
				</View>
				<View style={[styles.LinkH]}>
					<TouchableOpacity onPress={() => router.push('./register')}>
						<Text style={styles.fontT}>Register</Text>
					</TouchableOpacity>
					<TouchableOpacity onPress={() => router.push('./register')}>
						<Text style={styles.fontT}>Forgot Password</Text>
					</TouchableOpacity>
				</View>
				<TouchableOpacity onPress={() => router.push('./register')}>
					<Text style={styles.btn}>Login</Text>
				</TouchableOpacity>
				<Image style={styles.desk} source={require("../assets/images/deskdoc.png")} />


			</View>
		</View>
	);
};

const styles = StyleSheet.create({
	caresync: {
		fontSize: 36,
		fontWeight: "700",
		fontFamily: "MontaguSlab144pt-Bold",
		color: "rgba(92, 167, 136, 0.84)",
		textAlign: "center",
		paddingBottom: 20
	},
	connectingHealthcareSeamless: {
		fontSize: 20,
		fontWeight: "300",
		fontFamily: "MontaguSlab144pt-Light",
		color: "#000",
		textAlign: "center",
	},
	caresyncParent: {
		flex: 1,
	},
	bodCk: {
		borderColor: "rgba(92, 167, 136, 0.84)",
		borderWidth: 3,
		borderRadius: 10,
	},
	inpcon: {
		alignItems: 'center',
		padding: 20,
		gap: 10
	},
	eachIn: {
		flexDirection: 'row',
		alignItems: 'center',
		gap: 25,
		paddingLeft: 10,
	},
	Imgset: {
		width: 25,
		height: 27
	},
	LinkH: {
		flexDirection: 'row',
		gap: 50
	},
	fontT: {
		fontFamily: "MontaguSlab144pt-Light",
		color: "rgba(92, 167, 136, 0.84)",
	},
	spacer1: {
		height: '10%'
	},
	spacer2: {
		height: '20%'
	},
	btn: {
		backgroundColor: "rgba(92, 167, 136, 0.84)",
		fontFamily: "MontaguSlab144pt-Bold",
		color: "white",
		padding: 10,
		paddingLeft: 20,
		paddingRight: 20,
		borderRadius: 10,
	},
	desk: {
		padding: 0
	},
	txt: {
		width: 200,     // Fixed width
		height: 40,     // Fixed height
		padding: 10
	}

});

export default Frame;

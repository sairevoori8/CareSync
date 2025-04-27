import * as React from "react";
import {Text, StyleSheet, View} from "react-native";

const Register = () => {
  	
  	return (
    		<View style={[styles.register,styles.wrapper]}>
      			<View style={styles.createAccountParent}>
        				<Text style={styles.createAccount}>Create Account</Text>
        				<Text style={styles.aSmallStep}>A small step towards seamless health integration</Text>
        				<View style={styles.groupParent}>
          					<View style={styles.createUsernameParent}>
            						<Text style={[styles.createUsername, styles.createTypo]}> Create Username</Text>
            						<View style={[styles.groupChild, styles.groupLayout]} />
          					</View>
          					<View style={[styles.createPasswordParent, styles.parentPosition]}>
            						<Text style={[styles.createPassword, styles.createTypo]}> Create Password</Text>
            						<View style={[styles.groupItem, styles.groupLayout]} />
          					</View>
          					<View style={styles.createPasswordGroup}>
            						<Text style={[styles.createUsername, styles.createTypo]}> Confirm password</Text>
            						<View style={[styles.groupInner, styles.groupLayout]} />
          					</View>
          					<View style={[styles.patientIdParent, styles.parentPosition]}>
            						<Text style={[styles.patientId, styles.createTypo]}>Patient Id</Text>
            						<View style={[styles.rectangleView, styles.groupLayout]} />
          					</View>
          					<View style={[styles.rectangleParent, styles.groupChild1Layout]}>
            						<View style={[styles.groupChild1, styles.groupChild1Layout]} />
            						<Text style={[styles.submit, styles.createTypo]}>Submit</Text>
          					</View>
        				</View>
      			</View>
    		</View>);
};

const styles = StyleSheet.create({
  	createTypo: {
    		fontSize: 16,
    		color: "#000",
    		textAlign: "center",
    		position: "absolute"
  	},
  	groupLayout: {
    		height: 58,
    		borderWidth: 3,
    		borderColor: "rgba(92, 167, 136, 0.84)",
    		width: 236,
    		borderStyle: "solid",
    		borderRadius: 10,
    		position: "absolute",
    		backgroundColor: "#fff"
  	},
  	parentPosition: {
    		width: 236,
    		left: 39,
    		position: "absolute"
  	},
  	groupChild1Layout: {
    		height: 38,
    		width: 88,
    		position: "absolute"
  	},
  	createAccount: {
    		fontSize: 36,
    		fontWeight: "700",
    		fontFamily: "MontaguSlab144pt-Bold",
    		color: "rgba(92, 167, 136, 0.84)",
    		textAlign: "center",
  	},
  	aSmallStep: {
    		top: 66,
    		fontSize: 20,
    		height: 61,
    		color: "#000",
    		fontFamily: "MontaguSlab144pt-Light",
    		fontWeight: "300",
    		textAlign: "center",
    		left: 0,
    		width: 352,
    		position: "absolute"
  	},
  	createUsername: {
    		fontFamily: "MontaguSlab144pt-Light",
    		fontWeight: "300",
    		fontSize: 16,
    		top: 0,
    		left: 0
  	},
  	groupChild: {
    		left: 1,
    		top: 28,
    		borderWidth: 3,
    		borderColor: "rgba(92, 167, 136, 0.84)"
  	},
  	createUsernameParent: {
    		width: 237,
    		height: 86,
    		left: 39,
    		top: 24,
  	},
  	createPassword: {
    		left: 1,
    		fontFamily: "MontaguSlab144pt-Light",
    		fontWeight: "300",
    		fontSize: 16,
    		top: 0
  	},
  	groupItem: {
    		top: 28,
    		borderWidth: 3,
    		borderColor: "rgba(92, 167, 136, 0.84)",
    		left: 0
  	},
  	createPasswordParent: {
    		top: 125,
    		height: 86
  	},
  	groupInner: {
    		left: 4,
    		top: 28,
    		borderWidth: 3,
    		borderColor: "rgba(92, 167, 136, 0.84)"
  	},
  	createPasswordGroup: {
    		top: 226,
    		left: 37,
    		width: 240,
    		height: 86,
    		position: "absolute"
  	},
  	patientId: {
    		left: 7,
    		width: 87,
    		height: 28,
    		fontFamily: "MontaguSlab144pt-Light",
    		fontWeight: "300",
    		fontSize: 16,
    		top: 0
  	},
  	rectangleView: {
    		borderWidth: 3,
    		borderColor: "rgba(92, 167, 136, 0.84)",
    		top: 24,
    		left: 0
  	},
  	patientIdParent: {
    		top: 324,
    		height: 82
  	},
  	groupChild1: {
    		backgroundColor: "#b1e6c3",
    		borderColor: "#b1e6c3",
    		borderWidth: 2,
    		borderStyle: "solid",
    		width: 88,
    		borderRadius: 10,
    		left: 0,
    		top: 0
  	},
  	submit: {
    		top: 8,
    		left: 13,
    		fontFamily: "MontaguSlab144pt-Regular"
  	},
  	rectangleParent: {
    		top: 421,
    		left: 113
  	},
  	groupParent: {
    		top: 147,
    		left: 19,
    		backgroundColor: "rgba(92, 167, 136, 0.84)",
    		width: 314,
    		height: 483,
    		borderRadius: 10,
    		position: "absolute"
  	},
  	createAccountParent: {
        height: 630,
        width: 352,
        alignItems: 'center',
  	},
  	shape: {
    		top: 901,
    		borderRadius: 100,
    		backgroundColor: "#181818",
    		width: 100,
    		height: 4,
    		position: "absolute"
  	},
  	register: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 40, 
        backgroundColor: '#fff', 
      },
    wrapper: {
        width: '100%',
        justifyContent: 'center',
        alignItems: 'center',
    }
});

export default Register;

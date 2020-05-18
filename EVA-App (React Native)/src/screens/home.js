/* eslint-disable react-native/no-inline-styles */
import React, {useState, useEffect, useRef} from 'react';
import {
  Text,
  Alert,
  View,
  ScrollView,
  AsyncStorage,
  Dimensions,
  Image,
  TextInput,
} from 'react-native';
import back from '../assets/26984.jpg';
import Icon from 'react-native-vector-icons/FontAwesome';
const {width, height} = Dimensions.get('window');
import {Button, Appbar} from 'react-native-paper';

const axios = require('axios');

export default function Home() {
  const refScroll = useRef();
  var [question, setQuestion] = useState('');
  var [chat, setChat] = useState([]);
  var [key, setKey] = useState(0);
  function ask() {
    if (question === '') return;
    console.log('Packaging and sending');
    var payload = chat;
    var query = question;
    payload.push({query: query, response: ''});
    setChat(payload);
    setQuestion('');
    axios
      .get(`http://3.87.126.120:7000/response?question=${query}`)
      .then(async (response) => {
        payload.pop();
        console.log('RESPONSE', response);
        console.log('DATA', response.data);
        if (response.data.answer === undefined) {
          payload.push({query: query, response: response.data});
        } else {
          payload.push({query: query, response: response.data.answer});
        }
        console.log(payload);
        setChat(payload);
        await AsyncStorage.setItem('chat', JSON.stringify(payload));
        setKey(key === 0 ? 1 : 0);
      })
      .catch((err) => console.log(err));
  }
  const _onChangeSearch = (query) => setQuestion(query);
  const fetchChat = async () => {
    await AsyncStorage.getItem('chat').then((res) => {
      if (res !== null) {
        setChat(JSON.parse(res));
      }
    });
  };
  const clearChat = async () => {
    Alert.alert(
      'You are about to delete this chat with me ',
      'Do you want to proceed ? ',
      [
        {
          text: 'Yes',
          onPress: async () => {
            await AsyncStorage.removeItem('chat');
            Alert.alert('Sad to delete our memories  :(');
            setChat([]);
            setKey(key === 0 ? 1 : 0);
          },
        },
        {
          text: 'No',
          onPress: () => {
            Alert.alert('I am happy that you have changed your decision  :)');
          },
        },
      ],
    );
  };

  useEffect(() => {
    fetchChat();
  }, []);
  return (
    <>
      <Appbar.Header
        dark
        statusBarHeight={5}
        style={{backgroundColor: '#222', textAlign: 'center'}}>
        <Appbar.Content title="EVA Chatbot" />
        <Appbar.Action icon="delete" onPress={clearChat} />
      </Appbar.Header>
      <View style={{flex: 1, backgroundColor: 'transparent'}}>
        <View>
          <Image
            style={{
              height: height,
              width: width,
              position: 'absolute',
              top: 0,
              left: 0,
            }}
            source={back}
          />
        </View>
        <ScrollView
          style={{flex: 1, backgroundColor: 'transparent'}}
          key={key}
          ref={refScroll}
          onContentSizeChange={() =>
            refScroll.current.scrollToEnd({animated: true})
          }>
          {chat.length === 0 || chat === [] ? (
            <Text style={styles.bot}>
              Hi I am EVA! 🤖{'\n'} It will be nice talking to you 😊{'\n'}Let's
              Get Started 😎
            </Text>
          ) : (
            <>
              <View
                style={{
                  alignSelf: 'flex-start',
                  margin: 10,
                  flexDirection: 'row',
                  flexWrap: 'wrap',
                }}>
                <Icon name="rocket" />
                <Text style={styles.bot}>
                  Hi I am EVA! 🤖{'\n'} It will be nice talking to you 😊{'\n'}
                  Let's Get Started 😎
                </Text>
              </View>
              {chat.map(({query, response}) => {
                return (
                  <>
                    <View
                      style={{
                        alignSelf: 'flex-end',
                        margin: 10,
                        flexDirection: 'row',
                        flexWrap: 'wrap',
                      }}>
                      <Text style={styles.user}>{query}</Text>
                      <Icon name="user" />
                    </View>
                    {response !== '' ? (
                      <View
                        style={{
                          alignSelf: 'flex-start',
                          margin: 5,
                          flexDirection: 'row',
                          flexWrap: 'wrap',
                        }}>
                        <Icon name="rocket" />
                        <Text style={styles.bot}>{response}</Text>
                      </View>
                    ) : (
                      <>
                        <View
                          style={{
                            alignSelf: 'flex-start',
                            margin: 10,
                            flexDirection: 'row',
                            flexWrap: 'wrap',
                          }}>
                          <Icon name="rocket" />
                          <Text style={styles.bot}>Thinking...</Text>
                        </View>
                      </>
                    )}
                  </>
                );
              })}
            </>
          )}
        </ScrollView>
        <View
          style={{
            flexDirection: 'row',
            flexWrap: 'wrap',
            alignItems: 'center',
            marginBottom: 5,
          }}>
          <View
            style={{
              marginRight: 5,
              marginLeft: 5,
              flex: 1,
              backgroundColor: '#666',
              borderWidth: 1,
              borderRadius: 20,
              maxheight: 10,
              // borderColor: '#E91E63',
              // width: '80%',
              padding: 5,
              // backgroundColor: '#FFEB3B',
            }}>
            <TextInput
              Label="Type a Message"
              placeholder="Type a message"
              onChangeText={_onChangeSearch}
              value={question}
              underlineColorAndroid="rgba(0,0,0,0) !important"
              style={{
                color: '#000',
                color: 'white',
                borderBottomWidth: 0,
                height: 40,
                backgroundColor: 'transparent',
              }}
            />
          </View>
          <Button
            dark
            small
            mode="contained"
            color="black"
            onPress={ask}
            style={{
              backgroundColor: '#cc0044',
              textAlign: 'center',
              justifyContent: 'center',
              height: 50,
              borderRadius: 50,
              alignContent: 'center',
              alignItems: 'center',
            }}>
            <Icon name="send" />
          </Button>
        </View>
      </View>
    </>
  );
}

const styles = {
  user: {
    margin: 2,
    backgroundColor: '#222',
    color: 'white',
    padding: 12,
    borderRadius: 15,
    width: (4 * width) / 7,
    borderBottomRightRadius: 0,
  },
  bot: {
    margin: 2,
    backgroundColor: '#cc3345',
    color: 'black',
    padding: 12,
    borderRadius: 15,
    width: (4 * width) / 7,
    borderBottomLeftRadius: 0,
  },
};

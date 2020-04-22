#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n) {
    return document[n - 1][m - 1][k - 1];
}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m) { 
    return document[m - 1][k - 1];
}

char*** kth_paragraph(char**** document, int k) {
    return document[k - 1];
}

char** split(char* text, char delim) {
    assert(text != NULL);
    char** result = malloc(1*sizeof(char*));
    int size = 1;
    
    char* temp = strtok(text, &delim);
    *result = temp;
    
    while(temp != NULL) {
        size++;
        result = realloc(result,size*sizeof(char*));
        temp = strtok(NULL, &delim);
        result[size-1] = temp;
    }
    return result;
}

char**** get_document(char* text) {
    char** paragraphs = split(text, '\n');
    int nParagraphs = 0;
    while (paragraphs[nParagraphs++] != NULL);

    char**** document = malloc((nParagraphs + 1) * sizeof(char***));
    document[nParagraphs] = NULL;

    int i = 0;
    while (paragraphs[i] != NULL) {
        char** sentences = split(paragraphs[i], '.');
        int nSentences = 0;
        while (sentences[nSentences++] != NULL);

        document[i] = malloc((nSentences + 1) * sizeof(char**));
        document[i][nSentences] = NULL;

        int j = 0;
        while (sentences[j] != NULL) {
            document[i][j] = split(sentences[j], ' ');
            j++;
        }
        i++;
    }

    return document;
}

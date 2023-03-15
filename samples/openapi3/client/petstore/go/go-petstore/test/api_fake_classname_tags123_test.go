/*
OpenAPI Petstore

Testing FakeClassnameTags123ApiService

*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech);

package petstore

import (
	"context"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"testing"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func Test_petstore_FakeClassnameTags123ApiService(t *testing.T) {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)

	t.Run("Test FakeClassnameTags123ApiService TestClassname", func(t *testing.T) {

		t.Skip("skip test")  // remove to run test

		resp, httpRes, err := apiClient.FakeClassnameTags123Api.TestClassname(context.Background()).Execute()

		require.Nil(t, err)
		require.NotNil(t, resp)
		assert.Equal(t, 200, httpRes.StatusCode)

	})

}
